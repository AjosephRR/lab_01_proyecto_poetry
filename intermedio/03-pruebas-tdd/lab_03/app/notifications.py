from typing import Protocol


class NotificationGateway(Protocol):
    def send(self, to_email: str, message: str) -> bool: ...
