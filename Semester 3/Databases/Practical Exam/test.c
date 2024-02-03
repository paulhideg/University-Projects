#include <stdio.h>
#include <stdlib.h>

struct car {
    char make[20];
    int production_year;
    int kilometers;
    char damaged[4];
};

int main() {
    int n, i;
    int oldest_year = 9999, newest_year = 0;
    struct car *cars;
    FILE *file, *file2;

    file = fopen("cars.txt", "r");
    if (file == NULL) {
        printf("Error opening file");
        return 1;
    }

    fscanf(file, "%d", &n);
    cars = (struct car*) malloc(n * sizeof(struct car));

    for (i = 0; i < n; i++) {
        fscanf(file, "%s %d %d %s", cars[i].make, &cars[i].production_year, &cars[i].kilometers, cars[i].damaged);
        if (cars[i].production_year < oldest_year) {
            oldest_year = cars[i].production_year;
        }
        if (cars[i].production_year > newest_year) {
            newest_year = cars[i].production_year;
        }
    }

    if (newest_year - oldest_year > 20) {
        printf("Difference between oldest and newest car is more than 20 years\n");
    } else {
        printf("Difference between oldest and newest car is not more than 20 years\n");
    }

    printf("List of damaged cars:\n");
    for (i = 0; i < n; i++) {
        if (strcmp(cars[i].damaged, "YES") == 0) {
            printf("%s %d %d %s\n", cars[i].make, cars[i].production_year, cars[i].kilometers, cars[i].damaged);
        }
    }

    file2 = fopen("old_cars.txt", "w");
    if (file2 == NULL) {
        printf("Error opening file");
        return 1;
    }

    for (i = 0; i < n; i++) {
        if (2023 - cars[i].production_year > 5) {
            fprintf(file2, "%s %d %d %s\n", cars[i].make, cars[i].production_year, cars[i].kilometers, cars[i].damaged);
        }
    }

    fclose(file);
    fclose(file2);
    free(cars);

    return 0;
}
