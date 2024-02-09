from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # Retornar para um log
        # Enviar para um email de notificação
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )



    return HttpResponse(
        status_code=500,
        body=[{
            "error": "Server Error",
            "detail": str(error)
        }]
    )
