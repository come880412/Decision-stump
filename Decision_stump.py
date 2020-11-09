import numpy as np
import random

def Problem16():
    s = [-1,1]
    Eout_all = []
    for epochs in range(10000):
        x = np.random.uniform(-1,1,2)
        x_sort = np.sort(x)
        x_sort = np.round(x_sort,2)
        y = np.sign(x_sort).astype(int)
        E_in_min = 5000000
        for i in range(x.shape[0]-1):
            for sign in s:
                if x_sort[i] != x_sort[i+1]:
                    theta = (x_sort[i] + x_sort[i+1]) / 2
                    hypothesis = sign * np.sign(x_sort-theta).astype(int)
                    Ein = np.sum(hypothesis != y) / x.shape[0]
                    if round(Ein,2) < round(E_in_min,2):
                        E_in_min = Ein
                        theta_min = theta
                        s_min = sign
                    elif round(Ein,2) == round(E_in_min,2):
                        if (s_min + theta_min) > (sign + theta):
                            theta_min = theta
                            s_min = sign
        theta = -1
        for sign in s:
            hypothesis = sign * np.sign(x_sort-theta).astype(int)
            Ein = np.sum(hypothesis != y) / x.shape[0]
            if round(Ein,2) < round(E_in_min,2):
                E_in_min = Ein
                theta_min = theta
                s_min = sign
            elif round(Ein,2) == round(E_in_min,2):
                if (s_min + theta_min) > (sign + theta):
                    theta_min = theta
                    s_min = sign
        if s_min == 1:
            Eout = 1/2 * np.abs(theta_min)
        else:
            Eout = 1- (1/2 * np.abs(theta_min))

        Eout_all.append(Eout-E_in_min)
    
    Eout_all = np.array(Eout_all)
    Eout_mean = np.mean(Eout_all)
    print('Problem16:',round(Eout_mean,2))

def Problem17():
    s = [1,-1]
    Eout_all = []
    for epochs in range(10000):
        x = np.random.uniform(-1,1,20)
        x_sort = np.sort(x)
        x_sort = np.round(x_sort,2)
        y = np.sign(x_sort).astype(int)
        E_in_min = 5000000
        for i in range(x.shape[0]-1):
            for sign in s:
                if x_sort[i] != x_sort[i+1]:
                    theta = (x_sort[i] + x_sort[i+1]) / 2
                    hypothesis = sign * np.sign(x_sort-theta).astype(int)
                    Ein = np.sum(hypothesis != y) / x.shape[0]
                    if round(Ein,2) < round(E_in_min,2):
                        E_in_min = Ein
                        theta_min = theta
                        s_min = sign
                    elif round(Ein,2) == round(E_in_min,2):
                        if (s_min + theta_min) > (sign + theta):
                            theta_min = theta
                            s_min = sign
        theta = -1
        for sign in s:
            hypothesis = sign * np.sign(x_sort-theta).astype(int)
            Ein = np.sum(hypothesis != y) / x.shape[0]
            if round(Ein,2) < round(E_in_min,2):
                E_in_min = Ein
                theta_min = theta
                s_min = sign
            elif round(Ein,2) == round(E_in_min,2):
                if (s_min + theta_min) > (sign + theta):
                    theta_min = theta
                    s_min = sign
        if s_min == 1:
            Eout = 1/2 * np.abs(theta_min)
        else:
            Eout = 1- 1/2 * np.abs(theta_min)
        Eout_all.append(Eout-E_in_min)
    
    Eout_all = np.array(Eout_all)
    Eout_mean = np.mean(Eout_all)
    print('Problem17:',round(Eout_mean,2))

def Problem18():
    tau = 0.1
    s = [-1,1]
    Eout_all = []
    for epochs in range(10000):
        x = np.random.uniform(-1,1,2)
        x_sort = np.sort(x)
        x_sort = np.round(x_sort,2)
        y = np.sign(x_sort).astype(int)

        random_number = np.random.random(x_sort.shape[0])
        for j in range(x_sort.shape[0]):
            if random_number[j] <=tau:
                y[j] = -y[j]

        # x_out = np.random.uniform(-1,1,100000)
        # x_out = np.sort(x_out)
        # x_out = np.round(x_out,2)
        # y_noise = np.sign(x_out).astype(int)
        #noisy
        # random_number = np.random.random(x_out.shape[0])
        # for j in range(x_out.shape[0]):
        #     if random_number[j] <=tau:
        #         y_noise[j] = -y_noise[j]

        E_in_min = 5000000
        for i in range(x.shape[0]-1):
            for sign in s:
                if x_sort[i] != x_sort[i+1]:
                    theta = (x_sort[i] + x_sort[i+1]) / 2
                    hypothesis = sign * np.sign(x_sort-theta).astype(int)
                    Ein = np.sum(hypothesis != y) / x.shape[0]
                    if round(Ein,2) < round(E_in_min,2):
                        E_in_min = Ein
                        theta_min = theta
                        s_min = sign
                    elif round(Ein,2) == round(E_in_min,2):
                        if (s_min + theta_min) > (sign + theta):
                            theta_min = theta
                            s_min = sign
        theta = -1
        for sign in s:
            hypothesis = sign * np.sign(x_sort-theta).astype(int)
            Ein = np.sum(hypothesis != y) / x.shape[0]
            if round(Ein,2) < round(E_in_min,2):
                E_in_min = Ein
                theta_min = theta
                s_min = sign
            elif round(Ein,2) == round(E_in_min,2):
                if (s_min + theta_min) > (sign + theta):
                    theta_min = theta
                    s_min = sign
                    
        if s_min == 1:
            Eout = 1/2 * np.abs(theta_min)
        else:
            Eout = 1- 1/2 * np.abs(theta_min)
        Eout_noise = Eout * (1-2*tau) + tau
        # hypothesis = s_min * np.sign(x_out-theta_min).astype(int)
        # Eout_noise = np.sum(hypothesis != y_noise) / x_out.shape[0]
        Eout_all.append(Eout_noise-E_in_min)
    
    Eout_all = np.array(Eout_all)
    Eout_mean = np.mean(Eout_all)
    print('Problem18:',round(Eout_mean,2))

def Problem19():
    tau = 0.1
    s = [-1,1]
    Eout_all = []
    for epochs in range(10000):
        x = np.random.uniform(-1,1,20)
        x_sort = np.sort(x)
        x_sort = np.round(x_sort,2)
        y = np.sign(x_sort).astype(int)

        random_number = np.random.random(x_sort.shape[0])
        for j in range(x_sort.shape[0]):
            if random_number[j] <=tau:
                y[j] = -y[j]

        # x_out = np.random.uniform(-1,1,100000)
        # x_out = np.sort(x_out)
        # x_out = np.round(x_out,2)
        # y_noise = np.sign(x_out).astype(int)
        # #noisy
        # random_number = np.random.random(x_out.shape[0])
        # for j in range(x_out.shape[0]):
        #     if random_number[j] <=tau:
        #         y_noise[j] = -y_noise[j]

        E_in_min = 5000000
        for i in range(x.shape[0]-1):
            for sign in s:
                if x_sort[i] != x_sort[i+1]:
                    theta = (x_sort[i] + x_sort[i+1]) / 2
                    hypothesis = sign * np.sign(x_sort-theta).astype(int)
                    Ein = np.sum(hypothesis != y) / x.shape[0]
                    if round(Ein,2) < round(E_in_min,2):
                        E_in_min = Ein
                        theta_min = theta
                        s_min = sign
                    elif round(Ein,2) == round(E_in_min,2):
                        if (s_min + theta_min) > (sign + theta):
                            theta_min = theta
                            s_min = sign
        theta = -1
        for sign in s:
            hypothesis = sign * np.sign(x_sort-theta).astype(int)
            Ein = np.sum(hypothesis != y) / x.shape[0]
            if round(Ein,2) < round(E_in_min,2):
                E_in_min = Ein
                theta_min = theta
                s_min = sign
            elif round(Ein,2) == round(E_in_min,2):
                if (s_min + theta_min) > (sign + theta):
                    theta_min = theta
                    s_min = sign
                    
        if s_min == 1:
            Eout = 1/2 * np.abs(theta_min)
        else:
            Eout = 1- 1/2 * np.abs(theta_min)
        Eout_noise = Eout * (1-2*tau) + tau
        # hypothesis = s_min * np.sign(x_out-theta_min).astype(int)
        # Eout_noise = np.sum(hypothesis != y_noise) / x_out.shape[0]
        Eout_all.append(Eout_noise-E_in_min)
    
    Eout_all = np.array(Eout_all)
    Eout_mean = np.mean(Eout_all)
    print('Problem19:',round(Eout_mean,2))

def Problem20():
    tau = 0.1
    s = [-1,1]
    Eout_all = []
    for epochs in range(10000):
        x = np.random.uniform(-1,1,200)
        x_sort = np.sort(x)
        x_sort = np.round(x_sort,2)
        y = np.sign(x_sort).astype(int)

        random_number = np.random.random(x_sort.shape[0])
        for j in range(x_sort.shape[0]):
            if random_number[j] <=tau:
                y[j] = -y[j]

        # x_out = np.random.uniform(-1,1,100000)
        # x_out = np.sort(x_out)
        # x_out = np.round(x_out,2)
        # y_noise = np.sign(x_out).astype(int)
        #noisy
        # random_number = np.random.random(x_out.shape[0])
        # for j in range(x_out.shape[0]):
        #     if random_number[j] <=tau:
        #         y_noise[j] = -y_noise[j]

        E_in_min = 5000000
        for i in range(x.shape[0]-1):
            for sign in s:
                if x_sort[i] != x_sort[i+1]:
                    theta = (x_sort[i] + x_sort[i+1]) / 2
                    hypothesis = sign * np.sign(x_sort-theta).astype(int)
                    Ein = np.sum(hypothesis != y) / x.shape[0]
                    if round(Ein,2) < round(E_in_min,2):
                        E_in_min = Ein
                        theta_min = theta
                        s_min = sign
                    elif round(Ein,2) == round(E_in_min,2):
                        if (s_min + theta_min) > (sign + theta):
                            theta_min = theta
                            s_min = sign
        theta = -1
        for sign in s:
            hypothesis = sign * np.sign(x_sort-theta).astype(int)
            Ein = np.sum(hypothesis != y) / x.shape[0]
            if round(Ein,2) < round(E_in_min,2):
                E_in_min = Ein
                theta_min = theta
                s_min = sign
            elif round(Ein,2) == round(E_in_min,2):
                if (s_min + theta_min) > (sign + theta):
                    theta_min = theta
                    s_min = sign
                    
        if s_min == 1:
            Eout = 1/2 * np.abs(theta_min)
        else:
            Eout = 1- 1/2 * np.abs(theta_min)
        Eout_noise = Eout * (1-2*tau) + tau
        # hypothesis = s_min * np.sign(x_out-theta_min).astype(int)
        # Eout_noise = np.sum(hypothesis != y_noise) / x_out.shape[0]
        Eout_all.append(Eout_noise-E_in_min)
    
    Eout_all = np.array(Eout_all)
    Eout_mean = np.mean(Eout_all)
    print('Problem20:',round(Eout_mean,2))


if __name__ == "__main__":
    # Problem16()
    # Problem17()
    Problem18()
    Problem19()
    Problem20()
    

    
    