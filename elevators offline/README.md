# Elevators-offline
# smart elevator algorithm with pre request list
# the program: 
In this project we wanted to create an elevators algorithm system that will decrease the waiting time in total that take for an elevator to fill costumers request.
asuuming we recived all requset call list before the algorithm start to calculate and based on the call list that give us a full view of futures calls and based on that we can know better to allocate the correct elevator to give us the minimum waiting time for the calls.
 # reference material:
First, we want to introduce 3 article that helped us to make our code better even before we started to write it.
1. https://www.i-programmer.info/programmer-puzzles/203-sharpen-your-coding-skills/4561-sharpen-your-coding-skills-elevator-puzzle.html?start=1 . From Knuth Donald's article we got some ideas for idealize our algorithm for some evants.
https://paradigm.suss.edu.sg/the-smart-elevator-scheduling-algorithm-an/illustration-of-computational-intelligence . From this article we got the idea to make our algorithm "think" efficiency even if it is not the "fairest" decision for every person who call for elevator.
https://www.youtube.com/watch?v=xOayymoIl8U&ab_channel=SpanningTree . This video helped us understand better how elevator work and the decisoin system by a illustration of how elevators work.
 # algorithm "logic":
Because there is no limit for persons in elevator, we generally don't want to "waste" more than 2 elevators in each level - one for taking people up and one for taking people down.(except the first call that we want some elevators to be in the entrance floor for reducing the waiting time - we can assume that in the beginnig of the day there is a lot of calls from entrance floors)
We can use the list of calls so we can send an elevator even before the call will be accepted for gain more time of efficantly.
The elevator calls will sort by minimal or maximal floor requested source and not necessarily by requested time - because its not efficiant to stop for a passenger and after that go to the opposite direction to collect another passenger. In addition, in that time, on the way to the maximal or minimal request floor, we can get more calls from intermediate floors that the calls from there want to go in the same direction.
  # the algorithm:
Assuming there is only one elevator, and assuming the elevator is avaiable to go, we will boot the elevator to go for source of a call, as soon as possible to arrive before the call.
If the elevator is not aviable to go, we will send it to the source of the call if its in the same direction and the destination is in the same direction.
If the time of complete existing call takes more time to get the new passenger even if he is in the opposite way, the elevator will take him to and get the calls to their destination, by minumum to maximum (or opposite if its in the way down).
If there is 2 elevators, in the ideal case we want them to be in opposite directions to each other , so one elevator takes the up direction's calls to maximum request and the second elevator takes the opposite direction's calls to minimun request. After reach the finall destination the 2 elevators will swich directions.
If all the calls are in the same direction we will send an elevator to a middele floor to take care the calls around it and the another elevator will take the minimun or maximum floor.
Of course, as much elevator the building have, the less time take to take a call - as the elevators make the same algorithm like the 2 elevators algorithm and we choose the eficiant one by calculate who is the elevator that take the less time to take care of a call and not to make a dilay to the other calls if there is some.
