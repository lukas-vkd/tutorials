/** @odoo-module */

import { Reactive }  from "@web/core/utils/reactive";
import { EventBus } from "@odoo/owl";

export class ClickerModel extends Reactive {
    constructor() {
        super();
        this.clicks = 0;
        this.level = 0;
        this.clickBots = 0;
        this.bigbots = 0;
        this.bus = new EventBus();


        document.addEventListener("click", () => this.increment(1), true);
        setInterval(() => {
            this.clicks += this.clickBots * 10;
            this.clicks += this.bigbots * 100;
        }, 10000);


        
    }

    increment(inc) {
        this.clicks += inc;
        if (this.level < 1 && this.clicks >= 1000) {
            this.bus.trigger("MILESTONE_1k");
            this.level++;
        }
        if (this.level < 2 && this.clicks >= 5000) {
            this.bus.trigger("MILESTONE_5k");
            this.level++;
        }
    }

    buyClickBot() {
        const clickBotPrice = 1000;
        if (this.clicks < clickBotPrice) {
            return false;
        }
        this.clicks -= clickBotPrice;
        this.clickBots += 1;
    }


    buyBigBot() {
        const bigBotPrice = 5000;
        if (this.clicks < bigBotPrice) {
            return false;
        }
        this.clicks -= bigBotPrice;
        this.bigbots += 1;
    }
}