from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request, Response
from typing import Callable
import json

class ResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request:Request, call_next:Callable):
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

            return JSONResponse(content=custom_response_content, status_code=response.status_code, headers=header_map)
        except Exception as e:
            custom_response_content = {
                "status_code": 500,
                "status": "FAILED",
                'message': str(e)
            }
            return JSONResponse(content=custom_response_content, status_code=500)
