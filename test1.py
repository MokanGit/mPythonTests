print('Hello World!')

a : int = 3
b : str = '4'

def test (a : int, b : str) -> None:
    print (a,b)

test(2,'g2')


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, render_template
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=8000, debug=True)


  from fastapi import FastAPI
  app = FastAPI()
  
  @app.get('/')
  async def root():
      return {'message': 'Hello World'}

      // TODO #1"""sumary_line"""


         