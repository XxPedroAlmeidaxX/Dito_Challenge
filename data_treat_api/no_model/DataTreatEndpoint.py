import requests


# Returns a implementation to DataTreatEndpoint
class DataTreatEndpointFactory:
    use_mock = False
    instance = None

    # Decides which implementation returns according with use_mock value
    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = DataTreatEndpointMock() if cls.use_mock else DataTreatEndpointConcrete()

        return cls.instance


# Class that really accesses the endpoint
class DataTreatEndpointConcrete:

    endpoint_url = 'https://storage.googleapis.com/dito-questions/events.json'

    def result(self):
        return requests.get(url=self.endpoint_url)


# Class that mocks the access to the endpoint for test purposes
class DataTreatEndpointMock:

    def result(self):
        return RequestResultMock


# Behaves as the requests.get() result
class RequestResultMock:

    json_return = {
        "events": [
            {
                "event": "comprou-produto",
                "timestamp": "2016-09-22T13:57:32.2311892-03:00",
                "custom_data": [
                    {
                        "key": "product_name",
                        "value": "Camisa Azul"
                    },
                    {
                        "key": "transaction_id",
                        "value": "3029384"
                    },
                    {
                        "key": "product_price",
                        "value": 100
                    }
                ]
            },
            {
                "event": "comprou",
                "timestamp": "2016-09-22T13:57:31.2311892-03:00",
                "revenue": 250,
                "custom_data": [
                    {
                        "key": "store_name",
                        "value": "Patio Savassi"
                    },
                    {
                        "key": "transaction_id",
                        "value": "3029384"
                    }
                ]
            },
            {
                "event": "comprou-produto",
                "timestamp": "2016-09-22T13:57:33.2311892-03:00",
                "custom_data": [
                    {
                        "key": "product_price",
                        "value": 150
                    },
                    {
                        "key": "transaction_id",
                        "value": "3029384"
                    },
                    {
                        "key": "product_name",
                        "value": "Calça Rosa"
                    }
                ]
            },
            {
                "event": "comprou-produto",
                "timestamp": "2016-10-02T11:37:35.2300892-03:00",
                "custom_data": [
                    {
                        "key": "transaction_id",
                        "value": "3409340"
                    },
                    {
                        "key": "product_name",
                        "value": "Tenis Preto"
                    },
                    {
                        "key": "product_price",
                        "value": 120
                    }
                ]
            },
            {
                "event": "comprou",
                "timestamp": "2016-10-02T11:37:31.2300892-03:00",
                "revenue": 120,
                "custom_data": [
                    {
                        "key": "transaction_id",
                        "value": "3409340"
                    },
                    {
                        "key": "store_name",
                        "value": "BH Shopping"
                    }
                ]
            }
        ]
    }

    status_code = requests.codes.ok

    @classmethod
    def json(cls):
        return cls.json_return
