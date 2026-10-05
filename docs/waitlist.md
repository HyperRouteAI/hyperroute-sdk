# Waitlist sessions

A first `apply_beta` / `applyBeta` submission creates the application and sets an HttpOnly
`hr_waitlist_session` cookie. Updates to that email require the cookie, including partial survey
saves and upgrading to priority. Missing or incorrect cookies return HTTP 403. Old applications
without session ownership cannot be claimed using their email. Losing the cookie loses edit access.
The cookie is scoped to `/beta/apply`, SameSite=Strict, and Secure over HTTPS. Do not log or share it.

Python's synchronous and asynchronous clients retain it automatically when the same client
instance is reused. Check `persisted` before continuing: HTTP 200 alone does not confirm a save.

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    application = {"name": "Your name", "email": "you@example.com"}
    first = client.apply_beta(application)
    if first.data.get("persisted") is True:
        updated = client.apply_beta({**application, "track": "priority", "survey": {"note": "My use case"}})
```

For asynchronous Python, use `async with AsyncHyperRoute()` and await both calls on the same client.
Node's fetch does not retain cookies; forward the cookie explicitly through existing request options:

```javascript
import { HyperRoute } from '@hyperroute/sdk';

const client = new HyperRoute();
const application = { name: 'Your name', email: 'you@example.com' };
const first = await client.applyBeta(application);
const cookie = first.headers.get('set-cookie')?.split(';', 1)[0];
if (first.data.persisted === true && cookie) {
  const updated = await client.applyBeta(
    { ...application, track: 'priority', survey: { note: 'My use case' } },
    { headers: { cookie } },
  );
}
```

Do not retry a submission automatically after a lost response: the application may already exist,
while its cookie was not received. A 403 is not resolved by retrying or submitting the email again.
