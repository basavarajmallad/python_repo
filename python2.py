data={
    "region": "us-east-2",
    "accountId": "111222333444",
    "eventTriggerName": "trigger-group-us-east-instance-succeeded",
    "deploymentId": "d-75I7MBT7C",
    "instanceId": "arn:aws:ec2:us-east-2:444455556666:instance/i-496589f7",
    "lastUpdatedAt": "1446744207.564",
    "instanceStatus": "Succeeded",
    "lifecycleEvents": [
        {
            "LifecycleEvent": "ApplicationStop",
            "LifecycleEventStatus": "Succeeded",
            "StartTime": "1446744188.595",
            "EndTime": "1446744188.711"
        },
        {
            "LifecycleEvent": "BeforeInstall",
            "LifecycleEventStatus": "Succeeded",
            "StartTime": "1446744189.827",
            "EndTime": "1446744190.402"
        }
        # More lifecycle events might be listed here
    ]
}

# Printing the region
print(data["region"])
print(data["instanceId"])
print(data["region"])
print(data["instanceId"])
print(data["lifecycleEvents"][0]["LifecycleEvent"])
print(data["lifecycleEvents"][0]["EndTime"])
print(data["lifecycleEvents"][1]["StartTime"])
print(data["lifecycleEvents"][0]["LifecycleEventStatus"])
