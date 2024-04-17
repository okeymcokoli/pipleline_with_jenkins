import fire

def hello(name="John Travolta"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)