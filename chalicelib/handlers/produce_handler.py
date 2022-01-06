from http import HTTPStatus

from chalice import Response

class ProduceHandler:

    def get_produce(self) -> Response:
        return Response(
            status_code=HTTPStatus.OK,
            body={'produce': 'produce'},
            headers={'Content-type': 'text/plain'}
        )
