from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request, Response
from typing import Callable
from opentelemetry import trace
from datetime import datetime
from census_service.collectable_data import request_counter
import json

class ResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request:Request, call_next:Callable):
        if request.url.path == '/metrics':
            return await call_next(request)
        
        request_counter.inc(1)
        
        tracer = trace.get_tracer('drive_backend.tracer')

        request_start_time = datetime.now()

        request_body = (await request.body()).decode('utf-8')

        with tracer.start_as_current_span(f"[{request.method}] {request.url.path}") as drive_span:
            # drive_span.set_attribute('request.request_headers', json.dumps(request.headers))
            drive_span.set_attribute('request.method', request.method.lower())
            drive_span.set_attribute('request.query_params', json.dumps(request.query_params.__str__()))
            drive_span.set_attribute('request.start_time', request_start_time.isoformat())
            drive_span.set_attribute('request.request_body', json.dumps(request_body))
            try:
                response = await call_next(request)

                data = None
                if isinstance(response, Response):
                    body = b""
                    async for chunk in response.body_iterator:
                        body += chunk
                    data = body.decode('utf-8') if body else None
                    data = json.loads(data)

                custom_response_content = {
                    "status_code": response.status_code,
                    "status": None,
                    "data":None
                }

                if 200 >= response.status_code < 400:
                    custom_response_content['status'] = 'SUCCESS'
                    custom_response_content['data'] = data['detail'] if 'detail' in data else data
                    custom_response_content['message'] = None
                else:
                    custom_response_content['status'] = 'FAILED'
                    custom_response_content['message'] = data['detail'] if 'detail' in data else data
                
                header_map = {}
                for header, value in response.headers.items():
                    if header.lower() == 'content-length': continue
                    header_map[header] = value

                drive_span.set_attribute('request.status','SUCCESS')
                drive_span.set_attribute('request.status_code', response.status_code)
                drive_span.set_attribute('request.response_headers', json.dumps(header_map))
                drive_span.set_attribute('request.response_body', json.dumps(custom_response_content))
                drive_span.set_attribute('request.duration_in_milisecond', (datetime.now() - request_start_time).microseconds // 1000)
                return JSONResponse(content=custom_response_content, status_code=response.status_code, headers=header_map)
            except Exception as e:
                custom_response_content = {
                    "status_code": 500,
                    "status": "FAILED",
                    'message': str(e)
                }
                drive_span.set_attribute('request.status','FAILED')
                drive_span.set_attribute('request.status_code',500)
                drive_span.set_attribute('request.response_message', json.dumps(custom_response_content))
                drive_span.set_attribute('request.duration_in_milisecond', (datetime.now() - request_start_time).microseconds // 1000)
                return JSONResponse(content=custom_response_content, status_code=500)
