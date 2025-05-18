<template>
    <q-table hide-header flat class="w-full" @row-click="(e, row) => { $emit('row_clicked', row) }">
        <template v-slot:body-cell-value="props">
            <q-td :props="props">
                {{ props.row.label }}
            </q-td>
        </template>
        <template v-slot:no-data="">
            No matching commands
        </template>
    </q-table>
</template>

<script>
export default {
  data () {
    return {
      c: 0,
    }
  },
  methods: {
    inc() {this.c+=1;}
  }
}
</script>
