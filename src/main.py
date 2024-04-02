from js import Response
import requests

async def on_fetch(request, env):
    r = requests.get("https://blog.cloudflare.com/workers-ai-ga-huggingface-loras-python-support")
    return Response.new(r.text)