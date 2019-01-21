#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <map>
#include <locale>

using namespace std;

int main() {
    
    int binder_num;
    cin >> binder_num;

    // get and print each binder's recipes
    for (; binder_num > 0; --binder_num) {

        string binder_name = "";
        int ingredients_num, recipe_num, cost;
        getline(cin, binder_name);
        getline(cin, binder_name);
        cin >> ingredients_num >> recipe_num >> cost;
        map<string, int> ingredients;
        priority_queue<pair<int,string>, vector<pair<int, string> >, greater<pair<int, string> > > recipes;

        // get ingredient costs
        for (; ingredients_num > 0; --ingredients_num) {
            string ingredient;
            int ingredient_cost;
            cin >> ingredient >> ingredient_cost;
            ingredients[ingredient] = ingredient_cost;
        }

        // get each recipe
        for (; recipe_num > 0; --recipe_num) {
            string recipe_name;
            int recipe_cost = 0;
            getline(cin, recipe_name);
            getline(cin, recipe_name);
            cin >> ingredients_num;
            for (; ingredients_num > 0; --ingredients_num) {
                string ingredient;
                int num_ingredient;
                cin >> ingredient >> num_ingredient;
                recipe_cost += (ingredients[ingredient] * num_ingredient);
            }
            if (recipe_cost <= cost) {
                pair<int, string> recipe;
                recipe.first = recipe_cost;
                recipe.second = recipe_name; 
                recipes.push(recipe);
            }
        }

        // print out the recipes
        std::locale loc;
        for (string::size_type i = 0; i < binder_name.length(); ++i) {
            cout << std::toupper(binder_name[i], loc);
        }
        cout << endl;
        if (recipes.size() > 0) {
            while (!recipes.empty()) {
                pair<int, string> recipe;
                recipe = recipes.top();
                recipes.pop();
                cout << recipe.second << endl;
            }
        } else {
            cout << "Too expensive!" << endl;
        }
        // output a blank line
        cout << endl;

    }

}