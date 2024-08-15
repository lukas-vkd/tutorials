/** @odoo-module */

import { Component, useState} from "@odoo/owl";
import { TodoItem } from "./todoItem";
import { useAutofocus } from "../utils";

export class TodoList extends Component {
  static template = "awesome_owl.TodoList";
  static components = { TodoItem };

  setup() {
    this.nextId = 0;
    this.todos = useState([]);
    useAutofocus("todo_list_input")
  }

  addTodo(ev) {
    if (ev.keyCode === 13 && ev.target.value != "") {
      this.todos.push({
        id: this.nextId++,
        description: ev.target.value,
        isCompleted: false,
      });
      ev.target.value = "";
    }
  }
}
