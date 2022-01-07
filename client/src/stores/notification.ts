import { writable } from "svelte/store";

function createNotificationStore() {
    const { subscribe, set, update } = writable([]);

    return {
        subscribe,
        add : (notification) => update(notificationList => [...notificationList, notification]),
        remove : (notification) => update(notificationList => notificationList.filter(n => n !== notification))
    };
}

export const notifications = createNotificationStore();