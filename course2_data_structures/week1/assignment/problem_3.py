# Uses python3.
"""Network packet processing simulation.

Task: You are given a series of incoming network packets, and your task is to simulate
their processing. Packets arrive in some order. For each packet number i, you know the
time when it arrived Ai and the time it takes to process it Pi. There is only one process,
and it processes the incoming packets in the order of their arrival. there is only one
processor and it processes the incoming packets in the order of their arrival. If the
processor started to process some packet, it doesn't interript or stop until it finishes
the processing of this packet, and the processing of the packet i takes exactly Pi seconds.

The computer processing the packets has a network buffer of fixed size S. When packets
arrive, they are stored in the buffer before being processed. However, fi the buffer is
full when a packet arrives (there are S packets which have arrived before this packet,
and the computer hasn't finished processing any of them), it is dropped and won't be
processes at all. If several packets arrive at the same time, they are first all stored
in the buffer(some of them may be dropped because of that those which are desribed
later in the input.). The computer processes the packets in the order of their arrival
and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no
packets in the buffer, the computer just waits for the next packet to arrive. Note that
a packet leaves the buffer and frees the space in the buffer as soon as the computer
finishes processing it.

Input: The first line of the input contains the size S of the buffer and the number n
of incoming network packets. Each of the next n lines contains two numbers i-th line
contains the time of arrival Ai and the processing time Pi of the i-th packet. It is
guarranteed that the sequence of arrival times is non-decreasing (however, it can contain
the exact same times of arrival in milliseconds - in this case the packet which is
earlier in the input is considered to have arrived earlier).

Constraints:
All the numbers in the inputs are integers 1<= S <= 10^5, 1<= n <= 10^5, 0<= Ai <= 10^6,
0<= Pi <= 10^3, Ai <= Ai+1 for 1<= i <= n-1

Output:
For each packet output either the moment of time (in milliseconds) when the processor
began processing it or -1 if the packet was dropped (output the answers for the packets
in the same order as the packets are given in the input).
"""

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        while self.finish_time_:
            if self.finish_time_[0] <= request.arrival_time:
                self.finish_time_.pop(0)
            else:
                break
        if len(self.finish_time_) == self.size:
            return Response(True, -1)
        if not self.finish_time_:
            self.finish_time_ = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)
        last_element = self.finish_time_[-1]
        self.finish_time_.append(last_element + request.process_time)
        return Response(False, last_element)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    result = [str(response.start_time) if not response.dropped else '-1' for response in responses]
    print(' '.join(result))

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)