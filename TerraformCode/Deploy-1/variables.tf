variable  "target_node" {
    default =  "proxmox"
}
variable "clone" {
    description = "Template to clone from" 
    type = string
}
variable "ssh_key" {
    description = "SSH public key"
    type = string
    default =  "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBVWIb0okjcnObLrjAUOYf+ChFtD6pLjO1LKHAwe2ymi saade@MSI"
}
variable "proxmox_api_url" {
  type = string
}
variable "proxmox_api_token_id" {
  type = string
  sensitive = true
}
variable "proxmox_api_token_secret" {
  type = string
  sensitive = true
}


variable "vm_name" {
  description = "Name of the VM"
  type = string
}

variable "vm_id" {
  description = "ID of the VM"
  type = number
}

variable "cores" {
  description = "Number of CPU cores"
  type = number
  default = 2
}

variable "sockets" {
  description = "Number of CPU sockets"
  type = number
  default = 1
}

variable "memory" {
  description = "Memory size in MB"
  type = number
  default = 2048
}

variable "ip" {
  description = "IP address"
  type = string
}

variable "gw" {
  description = "Gateway"
  type = string
}

variable "disk_size" {
  description = "Disk size"
  type = string
  default = "8G"
}

variable "network_model" {
  description = "Network model"
  type = string
  default = "virtio"
}

variable "network_bridge" {
  description = "Network bridge"
  type = string
}

variable "network_tag" {
  description = "Network tag"
  type = number
}

variable "nameserver" {
  description = "Nameserver"
  type = string
  default = "8.8.8.8"
}

variable "network_config_type" {
  description = "Type of network configuration: static or dhcp"
  type = string
  default = "dhcp"
  validation {
    condition = contains(["static", "dhcp"], var.network_config_type)
    error_message = "network_config_type must be either 'static' or 'dhcp'"
  }
}