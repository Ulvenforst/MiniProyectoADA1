#ifndef ALGORITMOS_ORDENAMIENTO_CPP
#define ALGORITMOS_ORDENAMIENTO_CPP

template <typename T>
void mergeSort(std::vector<T>& vec, int left, int right, std::function<bool(const T&, const T&)> comp) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(vec, left, mid, comp);
        mergeSort(vec, mid + 1, right, comp);
        merge(vec, left, mid, right, comp);
    }
}

template <typename T>
void merge(std::vector<T>& vec, int left, int mid, int right, std::function<bool(const T&, const T&)> comp) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    std::vector<T> leftArray(n1);
    std::vector<T> rightArray(n2);

    for (int i = 0; i < n1; ++i)
        leftArray[i] = vec[left + i];
    for (int j = 0; j < n2; ++j)
        rightArray[j] = vec[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (comp(leftArray[i], rightArray[j])) {
            vec[k] = leftArray[i];
            i++;
        } else {
            vec[k] = rightArray[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        vec[k] = leftArray[i];
        i++;
        k++;
    }

    while (j < n2) {
        vec[k] = rightArray[j];
        j++;
        k++;
    }
}

#endif // ALGORITMOS_ORDENAMIENTO_CPP

