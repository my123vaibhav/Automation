from playwright.sync_api import sync_playwright

class APIClient:
    def __init__(self, base_url="https://reqres.in/"):
        self.playwright = sync_playwright().start()
        self.request = self.playwright.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Content-Type": "application/json",
                "x-api-key": "reqres-free-v1"
            }
        )

    def _normalize_endpoint(self, endpoint: str) -> str:
        # strip leading / to avoid dropping /api
        return endpoint.lstrip("/")

    def get(self, endpoint, **kwargs):
        return self.request.get(self._normalize_endpoint(endpoint), **kwargs)

    def post(self, endpoint, data=None, **kwargs):
        return self.request.post(self._normalize_endpoint(endpoint), data=data, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self.request.put(self._normalize_endpoint(endpoint), data=data, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        return self.request.patch(self._normalize_endpoint(endpoint), data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request.delete(self._normalize_endpoint(endpoint), **kwargs)

    def close(self):
        """Cleanup Playwright request context and stop Playwright."""
        self.request.dispose()
        self.playwright.stop()