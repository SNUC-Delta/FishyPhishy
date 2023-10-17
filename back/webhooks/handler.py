class WebhookClient:
    def __init__(self, webhooks: list[dict]):
        self.webhooks = {wh['name']: wh for wh in webhooks}

    def __call__(self, name: str, data: dict):
        if name not in self.webhooks:
            raise ValueError(f"Webhook {name} does not exist")
        webhook = self.webhooks[name]
        if webhook['method'] == "POST":
            # do post request
            pass
        elif webhook['method'] == "GET":
            # do get request
            pass
        else:
            raise ValueError(f"Invalid method {webhook['method']}")


client = WebhookClient([
    {
        "name": "webhook",  # this will act like a uniique id to the webhook
        "url": "https://joshuas-awesome-frontend/webhook/someendpoing",
        "method": "POST",  # or GET
        "schema": {
            "url": "string",
            "originalurl": "string",
            # ... etc, use "number" for int or float, "json" for arrays or dicts
        }
    },
    {
        # ...
    }
])

# Define below methods in your code

response = client.call("webhookname", {
    "url": "https://google.com",
    "originalurl": "https://google.com"
})
