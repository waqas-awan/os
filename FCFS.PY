def main():
	p=["p1","p2","p3"]
	at=[1,2,3]
	bt=[2,3,4]
	wt=[0,0,0]
	tt=[0,0,0]
	
	for i in range(0,3):
		for j in range(0,i):
			wt[i] += bt[j]	
	print("\nProcess\t\tBurst Time\tWaiting Time\tTurnaround Time")

	#calculating turnaround time
	for i in range(0,3):
		tt[i] = bt[i] + wt[i];
		print("\n", p[i], "\t\t" ,bt[i],  "\t\t" , wt[i] , "\t\t", tt[i])
		
if __name__ == "__main__":
	main()		