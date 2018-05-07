#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


#Sample data
activity =[
{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d84kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "21.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "96f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Johnson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "10.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "25.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "5.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "255.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "15.34 USD"},


{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805502g", "event_time": "2017-05-06T12:45:52.041Z", "customer_id": "96f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "96f50c7d8f42", "event_time": "2017-05-06T12:46:46.384Z", "last_name": "Johnson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d9f", "event_time": "2017-05-06T12:47:12.344Z", "customer_id": "96f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a43", "event_time": "2017-05-06T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "10.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-05-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "25.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-05-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "5.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-05-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "255.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-05-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "15.34 USD"},



{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e804002f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "80f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "80f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Williams", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "ac05e804102f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "80f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804202f", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "10.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804302f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "25.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804402f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "5.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e804502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "81f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "81f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Jones", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "ac05e804602f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "81f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804702f", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "12.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804802f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "28.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804902f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "9.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805506f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "82f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "82f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Brown", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b0d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "82f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a44", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "15.04 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a45", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "31.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a46", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "12.31 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805507f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "83f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "83f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Davis", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b6d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "83f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a47", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "18.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a48", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "34.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a49", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805508f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "84f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "84f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Miller", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d91f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "84f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a50", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "21.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a51", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "37.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a432", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "18.55 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e8055202f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "85f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "85f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Wilson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d92f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "85f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d12a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "24.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr52k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "40.4 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k21a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "22.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e2805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "86f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "86f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Moore", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b31d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "86f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a434", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "32.4 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a443", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "77.3 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a433", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e8058502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "87f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "87f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Thomas", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d98f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "87f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a543", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "01.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k14a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k13a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "05.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e835502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "88f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "88f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Taylor", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b5d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "88f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d12a4", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5Wk1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k31a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "59.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac04e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "89f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "89f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Anderson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede50b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "89f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d5a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "2.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a23", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "115.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e825502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "90f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "90f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Jackson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b3d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "90f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "07.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "66.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a73", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e845502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "91f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "91f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Harris", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b2d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "91f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "4.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a73", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e885502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "92f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "92f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Lane", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b4d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "92f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e8d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "137.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d90kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "49.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68g80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "95.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "cc05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "93f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "93f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Reed", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8sde40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "93f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80h5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "11.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80jr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "15.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80lr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "xc05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "94f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "94f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Thompson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8fde40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "94f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80g5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80hr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "251.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1z43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e505502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "95f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "95f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Martin", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40g1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "95f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a93", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "19.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1s43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "21.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1f43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "50.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e105502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "99f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "99f50c7s8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Chandra", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40d1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "99f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1f43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "17.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k4a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "28.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k7a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "95.34 USD"}
]

   
        

def TopXSimpleLTVCustomer(x,D):
    
    #D=activity   
    import pandas as pd
    #    import numpy as np
    from datetime import timedelta
    
    #Create the required Dataframes
    DF_SITE_VISIT=pd.DataFrame(columns=["customer_id","event_time","key","verb","tags"])
    DF_CUSTOMER=pd.DataFrame(columns=["key","event_time","verb","last_name","adr_city","adr_state"])
    DF_IMAGE=pd.DataFrame(columns=["customer_id","event_time","key","verb","camera_make","camera_model"])
    DF_ORDER=pd.DataFrame(columns=["customer_id","event_time","key","verb","total_amount"])
    
    #The analysis summary Dataframe
    DF_Customer_LTV=pd.DataFrame(columns=["customer_id","start_time","last_time","LTV"])
          
    #Fill the Dataframe according to the record type
    for record in D:
        if record["type"]=="SITE_VISIT":
            DF_SITE_VISIT=DF_SITE_VISIT.append(record,ignore_index=True)
            continue
        
        if record["type"]=="CUSTOMER":
            DF_CUSTOMER=DF_CUSTOMER.append(record,ignore_index=True)
            continue
        
        if record["type"]=="ORDER":
            DF_ORDER=DF_ORDER.append(record,ignore_index=True)
            continue
        
        if record["type"]=="IMAGE":
            DF_IMAGE=DF_IMAGE.append(record,ignore_index=True)
            continue
        
        print "Unsupprted input record: ",record
    
    
    #Calculating LVT for each customer
    for record in DF_CUSTOMER.iterrows():
        
        customer_id=record[1]["key"]
        #get the list of even associated to the customer_id above
        member_time=DF_SITE_VISIT[DF_SITE_VISIT["customer_id"]==customer_id]["event_time"]
        #correct the datetime format
        member_time=pd.to_datetime(member_time)
        
        member_time.sort_values()
    
        member_time=member_time.reset_index()
      
        #Customer with no visit
        if len(member_time)==0:
            rec_tmp={"customer_id":customer_id,"start_time":"","last_time":"","LTV":""}
            DF_Customer_LTV=DF_Customer_LTV.append(rec_tmp,ignore_index=True)
            continue
        
        #customer with only a single visit
        #the calculation could end up with a big LTV number
        #The Problem needs to be redefined for this scenario
        
        if len(member_time)==1: 
            #total spending per visit
            spend_per_visit=DF_ORDER[DF_ORDER["customer_id"]==customer_id]["total_amount"].str[:-3].astype("float").sum()
            
            order_time=member_time.iloc[0][1]
            
          
            LTV=spend_per_visit*52*10
    
            rec_tmp={"customer_id":customer_id,"start_time":order_time,"last_time":"","LTV":LTV}
            DF_Customer_LTV=DF_Customer_LTV.append(rec_tmp,ignore_index=True)
            continue
        
        first_visit=member_time.iloc[0][1]
        last_visit=member_time.iloc[-1][1]
   
        cnt_weeks=-1
        VisitsOrders=0
        
        while (True):
            
            #calculte next week
            next_week= first_visit+timedelta(days=7)
            cnt_weeks+=1
            
            #get the spending in the given week
            #spend_per_week=DF_ORDER[(DF_ORDER["customer_id"]==customer_id) and (pd.to_datetime(DF_ORDER["event_time"])>=first_visit) and (pd.to_datetime(DF_ORDER["event_time"])<=next_week)]["total_amount"].str[:-3].astype("float").sum()
            DF_Get_ID=DF_ORDER[(DF_ORDER["customer_id"]==customer_id)]
            DF_Get_Time0=DF_Get_ID[(pd.to_datetime(DF_Get_ID["event_time"])>=first_visit)]
            DF_Get_Time1=DF_Get_Time0[(pd.to_datetime(DF_Get_Time0["event_time"])<=next_week)]
            spend_per_week=DF_Get_Time1["total_amount"].str[:-3].astype("float").sum()
    
            #calculate the number of the visit in the given week
            #Number_Visits=DF_SITE_VISIT[(DF_SITE_VISIT["customer_id"]==customer_id) and (pd.to_datetime(DF_SITE_VISIT["event_time"])>=first_visit) and (pd.to_datetime(DF_SITE_VISIT["event_time"])<=next_week)]["event_time"].count()
            DF_Visits_ID=DF_SITE_VISIT[(DF_SITE_VISIT["customer_id"]==customer_id)]
            DF_Visits_Time0=DF_Visits_ID[(pd.to_datetime(DF_SITE_VISIT["event_time"])>=first_visit)]
            DF_Visits_Time1=DF_Visits_Time0[(pd.to_datetime(DF_SITE_VISIT["event_time"])<=next_week)]
            Number_Visits=DF_Visits_Time1["event_time"].count()
    
    
            #accumulate the orders per weeks
            VisitsOrders+=spend_per_week*Number_Visits #
            
            #last week
            if (next_week>last_visit):
                
                LTV=(VisitsOrders/cnt_weeks)*52*10.0
                rec_tmp={"customer_id":customer_id,"start_time":first_visit,"last_time":last_visit,"LTV":LTV}
                DF_Customer_LTV=DF_Customer_LTV.append(rec_tmp,ignore_index=True)
                break
            
            
          
            first_visit=next_week
        
    #print DF_Customer_LTV
    DF_Customer_LTV=DF_Customer_LTV.reset_index()
    DF_Customer_LTV.sort_values(by=["LTV"])
    DF_Customer_LTV= DF_Customer_LTV.sort_values(by=["LTV"],ascending=False)
    DF_Customer_LTV=DF_Customer_LTV.reset_index()
    #print DF_Customer_LTV
    return DF_Customer_LTV.iloc[0:x,2:]
    #DF_Customer_LTV.to_csv("Customer_LTV_Summary.csv")          
 
    
def main():
    print TopXSimpleLTVCustomer(5,activity)
       
            
if __name__ == '__main__':
    main()
#    
    
   