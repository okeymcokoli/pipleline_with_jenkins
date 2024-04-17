import fire

def hello(name="Jon Travolta"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)