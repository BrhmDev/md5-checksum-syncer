class NotificationService:
    def send_partner_notification(self, partner_id: str, type: str, text: str):
        print(f"Notification send to partner with id: {partner_id} | {type}: {text}")
