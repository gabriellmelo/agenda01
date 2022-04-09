from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = []

@app.route('/')
def prinicipal():
  return render_template(
    'index.html',
    contacts=contacts
  )
@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  
  contacts.append({'name' : title,'email' : email,'phone': phone})
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)