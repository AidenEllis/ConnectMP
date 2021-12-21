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
🍤 `ConnectMP` is the easiest and `efficient` way to share data between `Processes`. It's superfast, can handle big datas, can
create `multiple` data connection and really `simple` to get started. 🍰

🥐 `ConnectMP` is created out of pure `Frustration` of not being able to find a good solution to comminucate between Processes 🥨

### 🥗 Installation :
`via pip (recommended) :`
```commandline
pip install connectmp
```

## 🧇 Quickstart : (Docs)
> ⚠ Please read till the end to find what you're looking for!

### 🍤 connectmp.Process :
```python
from connectmp import Process
```
This `Process` class is same as `multiprocessing.Process`, it's just modified.
So, just use `connectmp.Process` where you would use `multiprocessing.Process`
```python
import time
from connectmp import Process


def do_something(connection):
    connection.data = "Sending Some Data."


def track_data(connection):
    time.sleep(1)
    print(f"Track i: {connection.data}")


if __name__ == '__main__':
    p1 = Process(target=do_something, connection=True)
    p2 = Process(target=track_data, args=(p1.connection,))

    p1.start()
    p2.start()
```
Just let me explain what's happening here. we have 2 functions, one is 
`do_something` which just sends data and `track_data` which recieves the data
and print's it. You can see in `p1` we are not pasing any argument but our
function `do_something` requires a `connection` argument.

When you enable `Process(connection=True)` Your target function will recieve
a keyword-argument value named `connection` which's value will contain the `Connection`
object. This `Connection` object is an individual connection. But You can of course share
this connection with other process.

in `p2` we shared the connection of our `p1` by `p1.connection` which 
returns the connection object of `p1`. In `track_data` function we just
recieve the data from `p1.connection`. You can send and recieve data from and to each other.

And yeah to send data all you do is assign the data to `connection.data` and also to
get data you have to do it with `connection.data`

## 

## ⚠ HOLD ON! You might also be looking for something like this down below!

So, if you're wondering if we can create `Conenction` seperately without creting
`Process` object? 🎉 YES! YES YOU CAN! with:

### 🥨 connectmp.Connection
```python
from connectmp import Connection
```
You can create your own `Connection` with this. Let me show you how:
```python
from connectmp import Connection

connection = Connection()
```
that's it! 🎉 You can create multiple `Connection`!
To use it just do it like how we did before, pass it as an argument and use it anywhere you want 🥂
> ⚠ NOTE: Make sure `Process(connection=True)` is not enabled, or it will conflict
with your function params. turn `Process(connection=True)` when you want to create another
`Connection` and get it in the function as an argument('connection').

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

Now each Process can communicate with each other! That's all
you need to know about `ConnectMP`. Hope this helped you 🎉

[🌟 Back to Top](#)
