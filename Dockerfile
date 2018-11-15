FROM ufoym/deepo:all-py36-cpu

RUN apt-get update && apt-get install curl -y
RUN curl -s https://0e6750164b49ef36966fe6ad82d4a3b6af2d562912857e19:@packagecloud.io/install/repositories/abeja/stable/script.deb.sh | bash
RUN apt-get install opencv3=3.3.0-2 -y
