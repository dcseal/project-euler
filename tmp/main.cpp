#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include <math.h>

int main ( int argc, char *argv[] )
{
    int id;
    double wtime;
    printf ( "\n" );
    printf ( " C/OpenMP version\n" );
    printf ( "\n" );
    printf ( " Number of processors available = %d\n", omp_get_num_procs ( ) );
    printf ( " Max Number of threads = %d\n", omp_get_max_threads ( ) );
    wtime = omp_get_wtime ( );

//#pragma omp num_threads(2);
//#pragma omp parallel default(shared) private(id)
//  {
        id = omp_get_thread_num ( );

    
    int max = 1280;
#pragma omp parallel for
        for (int i=1; i < max; i++) 
        for (int j=1; j < max; j++) 
        for (int k=1; k < max; k++) 
        {
            double p = (double) i;
        }
        printf (" This is process %d\n", id );
//  }

    // Finish up by measuring the elapsed time.
    wtime = omp_get_wtime ( ) - wtime;
    printf ( "\n" );
    printf ( " Normal end of execution.\n" );
    printf ( "\n" );
    printf ( " Elapsed wall clock time = %f\n", wtime );
    return 0;
}
