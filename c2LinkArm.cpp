

/*  A class to contain all the information that needs to
    be passed around between these functions, and can
    encapsulate it and hide it from the Python interface.
 
    Written by Travis DeWolf (May, 2013)
*/
class Sim {
    /* Very simple class, just stores the variables we
    need for simulation, and has 2 functions. Reset
    resets the state of the simulation, and step steps it
    forward. Tautology ftw!*/
 
    double* params;
    double dt, t0;
    double u0[NINP], other_out[NOUT+1], y[NOUT];
    double w[1 + 2 * NEQ + NPAR + NDFA + NEVT];
 
    SolverStruct S;
 
    public:
        Sim(double dt_val, double* params_pointer);
        void reset(double* out, double* ic);
        void step(double* out, double* u);
};
 
Sim::Sim(double dt_val, double* params_pointer)
{
    t0 = 0.0; // set up start time
    dt = dt_val; // set time step
    for (int i = 0; i < NINP; i++)
        u0[i] = 0.0; // initial control signal
 
    params = params_pointer; // set up parameters reference
 
    /* Setup */
    S.w = w;
    S.err = 0;
}
 
void Sim::reset(double* out, double* ic)
{
    SolverSetup(t0, ic, u0, params, y, dt, &S);
 
    /* Output */
    out[0] = t0;
        for(int j = 0; j < NOUT; j++)
            out[j + 1] = y[j];
}
 
void Sim::step(double* out, double* u)
/* u: control signal */
{
    for (int k = 0; k < NOUT; k++)
        out[k] = *dsn_undef; // clear values to nan
 
    /* Integration loop */
    /* Take a step with states */
    EulerStep(u, &S);
 
    if (S.err <= 0)
    {
        /* Output */
        SolverOutputs(y, &S);
 
        out[0] = S.w[0];
        for(long j = 0; j < NOUT; j++)
            out[j + 1] = y[j];
    }
}
 
int main (void)
{
    FILE *fd;
 
    double *ic, *p, *out;
    char* errbuf;
    long i, j, outd;
    long internal = 0;
 
    double dt = 0.00001;
 
    int time_steps = 1000000;
    double u[NINP];
    for (int k = 0; k < NINP; k++) u[k] = .1;
 
    fd = fopen("output.dat", "w");
 
    Sim sim = Sim(dt, NULL);
    sim.reset(out, NULL); // ic = NULL, use default start state
 
    for(i=0;i<time_steps;i++)
    {
        sim.step(out, u);
        fprintf(fd,"%lf ",out[0]);
        for(j=0;j<NOUT;j++)
        {
            fprintf(fd,"%lf ",out[j+1]);
        }
        fprintf(fd, "\n");
    }
 
    fclose(fd);
 
    return 0;
}