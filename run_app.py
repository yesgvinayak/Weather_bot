from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxp-689345538407-687507240517-681154369633-e93b351aacc92f69db8d0179b687d13f',
							'xoxb-689345538407-689353665159-hlXV4P2Djt4xr8f3gypZuyYZ',
							'xoxb-689345538407-689353665159-hlXV4P2Djt4xr8f3gypZuyYZ')
                           

agent.handle_channels([input_channel], 5004, serve_forever=True)