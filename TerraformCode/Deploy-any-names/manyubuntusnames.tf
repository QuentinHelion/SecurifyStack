resource "proxmox_vm_qemu" "ManyUbuntus" {
  count = length(var.hostnames)
  desc = "Test Many Ubuntu Cloud Init"
  name = var.hostnames[count.index]
  vmid = var.vm_id_start + count.index
  target_node = var.target_node
  clone = var.clone
  full_clone = true

  agent = 1
  os_type = "cloud-init"
  cores = var.cores
  sockets = var.sockets
  cpu = "host"
  memory = var.memory
  scsihw = "virtio-scsi-pci"
  bootdisk = "scsi0"

  disk {
    slot = 0
    size = var.disk_size
    type = "scsi"
    storage = "local-lvm"
  }

  network {
    model = var.network_model
    bridge = var.network_bridge
    tag = var.network_tag
  }

  ipconfig0 = var.network_config_type == "static" ? "ip=${var.ip_prefix}${count.index + 1}/24,gw=${var.gw}" : "dhcp"
  nameserver = var.nameserver

  sshkeys = var.ssh_key
}
