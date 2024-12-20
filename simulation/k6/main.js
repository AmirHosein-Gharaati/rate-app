import http from 'k6/http';
import {check, sleep} from 'k6';

import {MAXIMUM_POST_ID, BASE_URL} from "./config.js";

export const options = {
    scenarios: {
        random_rating: {
            executor: 'constant-vus',
            vus: 200,
            duration: '5m',
            exec: 'randomRating', // Function to execute for this scenario
        },
        mixed_rating: {
            executor: 'constant-vus',
            vus: 400,
            duration: '30s',
            exec: 'mixedRating', // Function to execute for this scenario
            startTime: '5m', // Start after the first scenario
        },
    },
};

export function randomRating() {
    const url = BASE_URL + '/rate';
    const payload = generateRandomRate(MAXIMUM_POST_ID);

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const response = http.post(url, payload, params);

    check(response, {
        'is status 201': (r) => r.status === 201,
    });

    sleep(Math.random() * 0.5);
}

export function mixedRating() {
    const url = BASE_URL + '/rate';
    const isSpecificRating = Math.random() < 0.5; // 50% chance for each type of rating

    const payload = isSpecificRating
        ? generateHighRateForPostOneAndTwo()
        : generateRandomRate(MAXIMUM_POST_ID);

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const response = http.post(url, payload, params);

    check(response, {
        'is status 201': (r) => r.status === 201,
    });

    sleep(Math.random() * 0.5);
}

function generateRandomRate(maxPostId = 1000) {
    return JSON.stringify({
        post: Math.floor(Math.random() * maxPostId) + 1,
        user_id: `device-id-${Math.floor(Math.random() * 1000000) + 1}`,
        score: Math.floor(Math.random() * 6), // Random score from 0 to 5
    });
}

function generateHighRateForPostOneAndTwo() {
    return JSON.stringify({
        post: Math.floor(Math.random() * 2) + 1,
        user_id: `device-id-${Math.floor(Math.random() * 1000000) + 1}`,
        score: 5,
    })
}