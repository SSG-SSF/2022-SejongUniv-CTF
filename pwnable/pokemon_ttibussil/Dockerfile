FROM ubuntu:16.04
RUN apt update
RUN apt install xinetd -y

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN useradd -mU pokeymon

COPY ./pokemon_ttibussil /home/pokeymon/pokemon_ttibussil

RUN chmod 750 /home/pokeymon /home/pokeymon/chall
RUN chown -R root:pokeymon /home/pokeymon
CMD ["/usr/sbin/xinetd","-dontfork"]