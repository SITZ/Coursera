// MP 1
#include	<wb.h>

__global__ void vecAdd(float * in1, float * in2, float * out, int len) {
	int index = threadIdx.x + blockDim.x * blockIdx.x;
	if (index < len) {
		out[index] = in1[index] + in2[index];
	}
}

int main(int argc, char ** argv) {
	wbArg_t args;
	int inputLength;
	float * hostInput1;
	float * hostInput2;
	float * hostOutput;
	float * deviceInput1;
	float * deviceInput2;
	float * deviceOutput;

	args = wbArg_read(argc, argv);

	wbTime_start(Generic, "Importing data and creating memory on host");
	hostInput1 = (float *) wbImport(wbArg_getInputFile(args, 0), &inputLength);
	hostInput2 = (float *) wbImport(wbArg_getInputFile(args, 1), &inputLength);
	hostOutput = (float *) malloc(inputLength * sizeof(float));
	wbTime_stop(Generic, "Importing data and creating memory on host");

	wbLog(TRACE, "The input length is ", inputLength);
	
	int inputSize = inputLength * sizeof(float);
      
	wbTime_start(GPU, "Allocating GPU memory.");
    //@@ Allocate GPU memory here
	
	cudaMalloc((void **) &deviceInput1, inputSize);
	cudaMalloc((void **) &deviceInput2, inputSize);
	cudaMalloc((void **) &deviceOutput, inputSize);

	wbTime_stop(GPU, "Allocating GPU memory.");

	wbTime_start(GPU, "Copying input memory to the GPU.");
    //@@ Copy memory to the GPU here
      
	cudaMemcpy(deviceInput1, hostInput1, inputSize, cudaMemcpyHostToDevice);
	cudaMemcpy(deviceInput2, hostInput2, inputSize, cudaMemcpyHostToDevice);
  
	wbTime_stop(GPU, "Copying input memory to the GPU.");
    
    //@@ Initialize the grid and block dimensions here

	dim3 DimGrid((inputLength - 1) / 256 + 1, 1, 1);
	dim3 DimBlock(256, 1, 1);
    
	wbTime_start(Compute, "Performing CUDA computation");
    //@@ Launch the GPU Kernel here

	vecAdd<<<DimGrid, DimBlock>>>(deviceInput1, deviceInput2, deviceOutput, inputLength);
  
	cudaThreadSynchronize();
	wbTime_stop(Compute, "Performing CUDA computation");
    
	wbTime_start(Copy, "Copying output memory to the CPU");
    //@@ Copy the GPU memory back to the CPU here
	
	cudaMemcpy(hostOutput, deviceOutput, inputSize, cudaMemcpyDeviceToHost);
  
	wbTime_stop(Copy, "Copying output memory to the CPU");

	wbTime_start(GPU, "Freeing GPU Memory");
    //@@ Free the GPU memory here
	
	cudaFree(deviceInput1);
	cudaFree(deviceInput2);
	cudaFree(deviceOutput);

	wbTime_stop(GPU, "Freeing GPU Memory");

	wbSolution(args, hostOutput, inputLength);

	free(hostInput1);
	free(hostInput2);
	free(hostOutput);

	return 0;
}
