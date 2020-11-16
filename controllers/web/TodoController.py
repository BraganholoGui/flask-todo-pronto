from flask import render_template, request, redirect
from models.Todo import todos

class TodoController():
  def index():
    return render_template(
      'index.html', todos=todos
    )

  def create():
    title = request.form.get('title')
    todos.append({
      'title': title, 'complete': False
    })
    return redirect('/')

  def delete(index):
    todos.pop(index)
    return redirect('/')

  def complete(index):
    todos[index]['complete'] = True
    return redirect('/')

  def update(index):
    title = request.form.get('title')
    todos[index]['title'] = title
    return redirect('/')