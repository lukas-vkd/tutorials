/** @odoo-module */

import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { CheckBox } from "@web/core/checkbox/checkbox";
import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { Component, useState, useExternalListener } from "@odoo/owl";

class ClickerSysTray extends Component {

    static template = "awesome_clicker.clicker_sys_tray";

    props = {};


    setup(){
        this.state = useState({value: 0} );

        useExternalListener(window, "click", this.increment, { capture: true });

    }

    increment(){
        this.state.value++;
    }

    //TODO check if it always increments by 10
    increment_10(){
        this.state.value = this.state.value + 9;
    }


}



export const systrayItem = {
    Component: ClickerSysTray,
};


registry.category("systray").add("awesome_clicker.clicker_sys_tray", systrayItem, { sequence: 0 });