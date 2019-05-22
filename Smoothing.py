import math
import statistics 
import Extract_Data as ED
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

"""

private resmoothDataset(dataset: Plottable.Dataset) {
      // When increasing the smoothing window, it smoothes a lot with the first
      // few points and then starts to gradually smooth slower, so using an
      // exponential function makes the slider more consistent. 1000^x has a
      // range of [1, 1000], so subtracting 1 and dividing by 999 results in a
      // range of [0, 1], which can be used as the percentage of the data, so
      // that the kernel size can be specified as a percentage instead of a
      // hardcoded number, what would be bad with multiple series.
      let factor = (Math.pow(1000, this.smoothingWeight) - 1) / 999;
      let data = dataset.data();
      let kernelRadius = Math.floor(data.length * factor / 2);

      data.forEach((d, i) => {
        let actualKernelRadius = Math.min(kernelRadius, i, data.length - i - 1);
        let start = i - actualKernelRadius;
        let end = i + actualKernelRadius + 1;

        // Only smooth finite numbers.
        if (!_.isFinite(d.scalar)) {
          d.smoothed = d.scalar;
        } else {
          d.smoothed = d3.mean(
              data.slice(start, end).filter((d) => _.isFinite(d.scalar)),
              (d) => d.scalar);
        }
      });
    }
        
        
        
        /**
     * Whether smoothing is enabled or not. If true, smoothed lines will be
     * plotted in the chart while the unsmoothed lines will be ghosted in
     * the background.
     *
     * The smoothing algorithm is a simple moving average, which, given a
     * point p and a window w, replaces p with a simple average of the
     * points in the [p - floor(w/2), p + floor(w/2)] range.  If there
     * aren't enough points to cover the entire window to the left, the
     * window is reduced to fit exactly the amount of elements available.
     * This means that the smoothed line will be less in and gradually
     * become more smooth until the desired window is reached. However when
     * there aren't enough points on the right, the line stops being
     * rendered at all.
     */ 
        
        

    /**
     * Weight (between 0.0 and 1.0) of the smoothing. This weight controls
     * the window size, and a weight of 1.0 means using 50% of the entire
     * dataset as the window, while a weight of 0.0 means using a window of
     * 0 (and thus replacing each point with themselves).
     *
     * The growth between 0.0 and 1.0 is not linear though. Because
     * changing the window from 0% to 30% of the dataset smooths the line a
     * lot more than changing the window from 70% to 100%, an exponential
     * function is used instead: http://i.imgur.com/bDrhEZU.png. This
     * function increases the size of the window slowly at the beginning
     * and gradually speeds up the growth, but 0.0 still means a window of
     * 0 and 1.0 still means a window of the dataset's length.
     */
     
     
     
"""



def exponential_function_for_smooth_coef(x):
    return ((1000.0**x)-1.0)/999.0
    
    
def smooth_plot(Y, factor = 0):
    factor = exponential_function_for_smooth_coef(factor)
    y_smoothed = []
    
    data_size = len(Y)
    kernelRadius = math.floor(data_size * factor / 2)
    
    for i in range(data_size):
        actualKernelRadius = min(kernelRadius, i, data_size - i - 1);
        start = i - actualKernelRadius;
        end = i + actualKernelRadius + 1;

        # Only smooth finite numbers
        
        if math.isnan(Y[i]):
            y_smoothed.append(Y[i])
        else:
            mean_val = statistics.mean(Y[start:end])
            y_smoothed.append(mean_val)  
        
    return y_smoothed

def draw_plot(X, Y):
    plt.plot(X, Y, '-') 
    plt.ylabel('Q')
    plt.xlabel('Iteration')
    plt.grid(True)
    
    blue_patch = mpatches.Patch(color = 'blue', label = 'DNC')
    red_patch = mpatches.Patch(color = 'red', label = 'LSTM')
    plt.legend(handles = [blue_patch, red_patch])
    
    plt.title(r"$\bf{Copy Task (Training)}$", fontsize = 14)
    
    plt.show()
    

def main():
    X, Y = ED.Extract_Data()
    Y = smooth_plot(Y)
    draw_plot(X, Y)
    
main()
     


    