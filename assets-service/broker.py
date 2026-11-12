def send_event(data: dict):
    message = f"[БРОКЕР] Отправлено событие ReadingAdded: {data}"
    print(message, flush=True) # flush=True заставляет консоль выводить текст сразу
    return message
