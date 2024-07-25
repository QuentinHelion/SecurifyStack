resource "proxmox_vm_qemu" "ManyUbuntus" {
  count = var.vm_count
  desc = "Test Many Ubuntu Cloud Init"
  name = "${var.base_name}-${count.index + 1}"
  vmid = var.start_vmid + count.index
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

  ipconfig0 = var.network_config_type == "dhcp" ? "ip=dhcp" : "ip=${var.start_ip}${count.index + 1}/24,gw=${var.gw}"
  nameserver = var.nameserver

  sshkeys = var.ssh_key
}
