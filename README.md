# fastlangbot
Fast API with Lang Chain, Open AI, React and ElasticSearch in a local environment(docker) chatbot

# To run
1 - navigate to the main project´s folder and run the ElasticSearch script by: sh run_elasticsearch.sh
2 - activate the virtual environment, by running the command source venv/bin/activate
3 - run the indexer for the ElasticSearch, navigate to the folder /src and by running the command python3 indexer.py
4 - run the front-end, by navigating to the folder /front and run the command npm start
5 - run the back-end, by running the command uvicorn app:app --reload (already with an active virtual environment)

# Interaction
Can be both using a simple front-end or by an integration(since it is a Fast Api, access localhost:8000/docs)

