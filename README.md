<a href="https://github.com/AidenEllis/Cligo"><p align="center"></a>
<img height=100 src="https://upstorage.pythonanywhere.com/api/storage/file/its_sakib/Public/Github/ConnectMP/connectmp_logo_original.png"/>

<p align="center">
  <strong>ConnectMP - Taking Multi-Process Data Sharing to the moon 🚀</strong>
</p>

<h3 align="center">
  <a href="https://github.com/AidenEllis/ConnectMP/blob/main/CONTRIBUTING.md">Contribute</a>
  <span> · </span>
  <a href="https://discord.gg/aw35Kb7uE7">Community</a>
  <span> · </span>
  <a href="https://github.com/AidenEllis/ConnectMP/">Documentation</a>
</h3>

---

## 🎫 Introduction :
🍤 `ConnectMP` is an simple, easy way to share data between `Processes` using DB. It's superfast, can handle big datas, can
create `multiple` data connection and really `simple` to get started. 🍰

🥐 `ConnectMP` is created out of pure `Frustration` of not being able to find a good solution to comminucate between Processes 🥨

### 🥗 Installation :
`via pip (recommended) :`
```commandline
pip install connectmp
```

## 🧇 Quickstart : (Docs)

### 🥨 connectmp.Connection
Let's see how to create a connection Object.

First, import this:
```python
from connectmp import Connection
```
You can create your own `Connection` with this. Let me show you how:
```python
from connectmp import Connection

connection = Connection()
```
that's it! 🎉 You can also create multiple `Connection` like this!
pass it as an argument and use it anywhere you want 🥂

Here's an example below:

#### 🌮 Example:
```python
import time
from connectmp import Process, Connection


def do_something(connection):
    connection.data = "Sending Some Data."


def track_data(connection):
    time.sleep(1)
    print(f"Track i: {connection.data}")


if __name__ == '__main__':
    conn = Connection()  # Creating connection
    
    p1 = Process(target=do_something, args=(conn,))
    p2 = Process(target=track_data, args=(conn,))

    p1.start()
    p2.start()
```

Here we created a `Connection` object named `conn`, and we created  2 `Process`. Both of then share the same `Connection` object so they can communicate with each other. In our
`do_something` function we send the data and in `track-data` function we get the data and print it out.

That's all you needed to know about `ConnectMP`. Hope this helped you 🎉

[🌟 Back to Top](#)
