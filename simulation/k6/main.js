import http from 'k6/http';
import {check} from 'k6';
import {sleep} from 'k6';

export const options = {
    scenarios: {
        normal_load: {
            executor: 'constant-vus',
            vus: 500, // Number of virtual users
            duration: '1m', // Test duration
        },
    },
};

export default function () {
    const url = 'http://localhost:8000/api/rate';
    const payload = JSON.stringify({
        post: Math.floor(Math.random() * 1000) + 1, // Random ID from 1 to 1000
        user_id: `device-id-${Math.floor(Math.random() * 1000000) + 1}`, // Random device ID
        score: Math.floor(Math.random() * 6), // Random score from 0 to 5
    });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const response = http.post(url, payload, params);

    // Check the response status
    check(response, {
        'is status 201': (r) => r.status === 201,
    });

    // Optional sleep to simulate real user think time
    sleep(Math.random() * 0.5); // Random delay between requests (up to 0.5 seconds)
}
