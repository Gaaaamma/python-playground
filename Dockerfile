FROM ubuntu:20.04

# Args
ARG MASTER_PW

# Install packages
RUN apt-get update && \
    yes | unminimize && \
    apt-get install -y tini iproute2 iputils-ping net-tools netcat && \
    apt-get install -y openssh-server sudo vim grep gawk rsync tmux man manpages manpages-dev manpages-posix manpages-posix-dev diffutils && \
    apt-get install -y gcc gcc-multilib g++ g++-multilib gdb make yasm nasm tcpdump libcapstone-dev python3 && \
    apt-get install -y libc6-dbg dpkg-dev && \
    apt-get install -y curl git zsh && \
    apt-get install -y python3 python3-pip python3-venv && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    mkdir /var/run/sshd && \
    apt-get install -y locales tzdata

# Set locale
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    /usr/sbin/locale-gen

# Set timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Add user/group, set empty password, and allow sudo
RUN useradd -m -s /bin/bash -G sudo tcyangzb && \
    echo "tcyangzb:$MASTER_PW" | chpasswd && \
    echo '%sudo ALL=(ALL) ALL' >> /etc/sudoers

# Expose SSH port
EXPOSE 22

# Run the service
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/sshd", "-D"]