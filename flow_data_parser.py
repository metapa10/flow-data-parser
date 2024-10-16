#!/usr/bin/env python
# coding: utf-8

# In[36]:


from typing_extensions import Protocol
import csv
from collections import defaultdict

def protocol_decimal_lookup(protocol_decimal_file):
  protocol_mapping = {}
  with open(protocol_decimal_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
      decimal = row['Decimal']
      protocol = row['Keyword']
      protocol_mapping[decimal] = protocol
  return protocol_mapping


def load_lookup_table(lookup_file):
    tag_mapping = {}
    with open(lookup_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dstport = row['dstport'].strip()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            tag_mapping[(dstport, protocol)] = tag
    return tag_mapping

def process_flow_logs(flow_log_file, tag_mapping, protocol_mapping):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(flow_log_file, mode='r', newline='') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip malformed lines

            dstport = parts[6]
            protocol = protocol_mapping.get(parts[7], 'Not Found').lower()
            key = (dstport, protocol)
            tag = tag_mapping.get(key, "Untagged")

            tag_counts[tag] += 1
            port_protocol_counts[key] += 1

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, mode='w', newline='') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            file.write(f"{tag},{count}\n")

        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            file.write(f"{port},{protocol},{count}\n")

def main(flow_log_file, lookup_file, protocol_decimal_file, output_file):
    tag_mapping = load_lookup_table(lookup_file)
    protocol_mapping = protocol_decimal_lookup(protocol_decimal_file)
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_file, tag_mapping, protocol_mapping)
    write_output(tag_counts, port_protocol_counts, output_file)

# Example usage:
if __name__ == "__main__":
    flow_log_file = 'flow.txt'
    lookup_file = 'lut.txt'
    protocol_decimal_file = 'protocol-numbers-1.csv'
    output_file = 'output_counts.csv'
    main(flow_log_file, lookup_file, protocol_decimal_file, output_file)

