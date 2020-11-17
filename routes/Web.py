from flask import Blueprint
from controllers.web.TodoController import TodoController

web = Blueprint('web', __name__)

@web.route('/')
def index():
  return TodoController.index()

@web.route('/create', methods=['POST'])
def create():
  return TodoController.create()

@web.route('/delete/<int:index>')
def delete(index):
  return TodoController.delete(index)

@web.route('/complete/<int:index>')
def complete(index):
  return TodoController.complete(index)

@web.route('/update/<int:index>', methods=['POST'])
def update(index):
  return TodoController.update(index)