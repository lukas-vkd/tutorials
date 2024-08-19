/** @odoo-module */

export function choose(list) {
	//what happends if the list is empty
	return list[Math.floor(Math.random() * list.length)];
}
