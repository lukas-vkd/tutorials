/** @odoo-module */
import { registry } from "@web/core/registry";
import { ClickerModel } from "./clicker_model";
import { useService } from "@web/core/utils/hooks";
const clickerService = {
    dependencies: ["effect"],
    start(env, services) {
        const clickerModel = new ClickerModel();
        const bus = clickerModel.bus;
        bus.addEventListener("MILESTONE_1k", () => {
            services.effect.add({
                message: "Milestone reached! You can now buy clickbots",
                type: "rainbow_man",
            });
        });
        bus.addEventListener("MILESTONE_5k", () => {
            services.effect.add({
                message: "Milestone reached! You can now buy bigbots",
                type: "rainbow_man",
            });
        });
        return clickerModel;
    },
};

registry.category("services").add("awesome_clicker.clicker", clickerService);
