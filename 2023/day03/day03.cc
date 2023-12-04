#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

std::vector<std::vector<char>> read(const std::string& fp) {
  std::ifstream file(fp);
  std::vector<std::vector<char>> data;
  std::string line;
  std::vector<char> row;

  while (std::getline(file, line)) {
    row.clear();
    for (const char& c : line) {
      row.push_back(c);
    }
    data.push_back(row);
  }

  file.close();

  return data;
}

std::vector<char> neighbors(const size_t& row, const size_t& col,
                            const std::vector<std::vector<char>>& data) {
  const int nrows = data.size();
  const int ncols = data[0].size();
  std::vector<char> result;

  for (int i = -1; i <= 1; ++i) {
    for (int j = -1; j <= 1; ++j) {
      if (i == 0 && j == 0) continue;

      int crow = row + i;
      int ccol = col + j;

      if (crow >= 0 && crow < nrows && ccol >= 0 && ccol < ncols) {
        result.push_back(data[crow][ccol]);
      }
    }
  }

  return result;
}

std::vector<std::vector<std::pair<size_t, size_t>>> number_indices(
    const std::vector<std::vector<char>>& data) {
  std::vector<std::vector<std::pair<size_t, size_t>>> indices;

  for (size_t i = 0; i < data.size(); ++i) {
    const std::vector<char>& row = data[i];
    std::vector<std::pair<size_t, size_t>> current_indices;

    for (size_t j = 0; j < row.size(); ++j) {
      if (std::isdigit(row[j])) {
        current_indices.emplace_back(i, j);
      } else if (!current_indices.empty()) {
        indices.push_back(current_indices);
        current_indices.clear();
      }
    }
    if (!current_indices.empty()) {
      indices.push_back(current_indices);
    }
  }

  return indices;
}

bool is_engine_part(const std::vector<std::vector<char>>& data,
                    const std::vector<std::pair<size_t, size_t>>& indices) {
  for (const auto& ij : indices) {
    for (const auto& nb : neighbors(std::get<0>(ij), std::get<1>(ij), data)) {
      if (!std::isdigit(nb) && nb != '.') {
        return true;
      }
    }
  }
  return false;
}

int part_number(const std::vector<std::vector<char>>& data,
                const std::vector<std::pair<size_t, size_t>>& indices) {
  std::vector<char> chars;
  for (const auto& ij : indices) {
    chars.push_back(data[std::get<0>(ij)][std::get<1>(ij)]);
  }
  return std::stoi(std::string(chars.begin(), chars.end()));
}

std::vector<std::pair<size_t, size_t>> gear_indices(
    const std::vector<std::vector<char>>& data) {
  std::vector<std::pair<size_t, size_t>> indices;

  for (size_t i = 0; i < data.size(); ++i) {
    const std::vector<char>& row = data[i];
    for (size_t j = 0; j < row.size(); ++j) {
      if (row[j] == '*') indices.emplace_back(i, j);
    }
  }

  return indices;
}

bool is_gear_neighbor(const std::vector<std::pair<size_t, size_t>>& number,
                      const std::pair<size_t, size_t>& gear) {
  for (const auto& ij : number) {
    for (int i = -1; i <= 1; ++i) {
      for (int j = -1; j <= 1; ++j) {
        if (i == 0 && j == 0) {
          continue;
        } else if (static_cast<int>(std::get<0>(ij)) + i ==
                       static_cast<int>(std::get<0>(gear)) &&
                   static_cast<int>(std::get<1>(ij)) + j ==
                       static_cast<int>(std::get<1>(gear))) {
          return true;
        }
      }
    }
  }
  return false;
}

std::vector<int> gear_neighbors(const std::pair<size_t, size_t>& gear,
                                const std::vector<std::vector<char>>& data) {
  std::vector<int> neighbors;
  for (const auto& ids : number_indices(data)) {
    if (is_gear_neighbor(ids, gear)) {
      neighbors.push_back(part_number(data, ids));
    }
  }
  return neighbors;
}

int main() {
  auto data = read("input.txt");

  int part1 = 0;
  for (const auto& ids : number_indices(data)) {
    if (is_engine_part(data, ids)) {
      part1 += part_number(data, ids);
    }
  }
  std::cout << "Part 1: " << part1 << std::endl;

  int part2 = 0;
  for (const auto& gear : gear_indices(data)) {
    auto neighbors = gear_neighbors(gear, data);
    if (neighbors.size() == 2) {
      part2 += neighbors[0] * neighbors[1];
    }
  }
  std::cout << "Part 2: " << part2 << std::endl;
}
